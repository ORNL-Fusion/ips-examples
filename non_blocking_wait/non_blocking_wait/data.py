import tensorflow
import adaptive

def function(x):
    return tensorflow.sin(tensorflow.exp(x))

class data(Component):
    def __init__(self, services, config)
        Component.__init__(self.services, config)

    def init(self, timeStamp=0.0):
        self.services.stage_input_files('model_config.json')
        self.config = adaptive.load_json('model_config.json')
        self.train_port = self.services.get_port('TRAIN')

    def step(self, timeStamp=0.0):
        lower_range = config['inputs'][0]['lower_range']
        upper_range = config['inputs'][0]['upper_range']]

        initial_data = adaptive.generate_uniform_data(10,
                                                      min=[lower_range],
                                                      max=[upper_range])

        initial_data = initial_data.numpy()
        initial_data[numpy.argmin(initial_data)] = lower_range
        initial_data[numpy.argmax(initial_data)] = upper_range

        training_data = {
            'x' : tensorflow.reshape(tensorflow.convert_to_tensor(initial_data, dtype=tensorflow.float32),shape),
            'y' : None
        }
        training_data['y'] = function(training_data['x'])

        adaptive.save_json('new_data.json', training_data)
        self.services.update_state()

        prediction_size = 1000

        pred_data = {'x': None, 'y': None}

        pred_data['x'] = tensorflow.linspace(training_min_x,
                                             training_max_x,
                                             prediction_size)
        pred_data['y'] = function(pred_data['x'])

        for i in range(10):
            wait = self.services.call_nonblocking(self.train_port)

            while true:
                try:
                    self.services.wait_call(wait, 'False')
                    break
                except:
                    None

                [new_points, err_est] = surrogate.surrogat_adapt_data(training_data, args['batch_size'])
                training_data['x'] = tensorflow.concat([training_data['x'],tensorflow.convert_to_tensor(new_points)],0)
                training_data['y'] = tensorflow.concat([training_data['y'],function(tensorflow.convert_to_tensor(new_points))],0)

            new_data = adaptive.load_json('new_data.json')

            training_data['x'] = tensorflow.concat([training_data['x'], new_data['x']],0)
            training_data['y'] = tensorflow.concat([training_data['y'], new_data['y']],0)
}
