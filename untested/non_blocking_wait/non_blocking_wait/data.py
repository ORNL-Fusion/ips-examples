from ipsframework import Component
import tensorflow
import adaptive
import numpy
import surrogate
import time

def function(x):
    return tensorflow.sin(tensorflow.exp(x))

def to_json_compat(database):
    json_data = {}
    for key in database:
        json_data[key] = database[key].numpy().tolist()
    return json_data

class data(Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)

    def init(self, timeStamp=0.0):
        self.services.stage_input_files('model_config.json')
        self.config = adaptive.load_json('model_config.json')
        self.train_port = self.services.get_port('TRAIN')

    def step(self, timeStamp=0.0):
        lower_range = self.config['inputs'][0]['lower_range']
        upper_range = self.config['inputs'][0]['upper_range']

        batch_size = 10

        initial_data = adaptive.generate_uniform_data(batch_size,
                                                      min=[lower_range],
                                                      max=[upper_range])

        initial_data = initial_data.numpy()
        initial_data[numpy.argmin(initial_data)] = lower_range
        initial_data[numpy.argmax(initial_data)] = upper_range

        training_data = {
            'x' : tensorflow.reshape(tensorflow.convert_to_tensor(initial_data, dtype=tensorflow.float32), (batch_size,)),
            'y' : None
        }
        training_data['y'] = function(training_data['x'])

        prediction_size = 1000

        for i in range(10):
            adaptive.save_json('new_data.json', to_json_compat(training_data))
            self.services.update_state()
            wait = self.services.call(self.train_port, 'init', timeStamp)
            wait = self.services.call_nonblocking(self.train_port, 'step', timeStamp)

            while True:
                try:
                    self.services.wait_call(wait, False)
                    print('new_data ready')
                    break
                except:
                    pass

                [new_points, err_est] = surrogate.surrogat_adapt_data(training_data, batch_size)
                new_points = tensorflow.reshape(tensorflow.convert_to_tensor(new_points), (len(new_points),))
                training_data['x'] = tensorflow.concat([training_data['x'], new_points], 0)
                training_data['y'] = tensorflow.concat([training_data['y'], function(tensorflow.convert_to_tensor(new_points))], 0)

                time.sleep(60)
                print('proxy_data')

            self.services.stage_state()
            new_data = adaptive.load_json('new_data.json')

            training_data['x'] = tensorflow.concat([training_data['x'], new_data['x']],0)
            training_data['y'] = tensorflow.concat([training_data['y'], function(new_data['x'])],0)
            timeStamp += 1.0
