from ipsframework import Component
import adaptive
import multiprocessing
import os
import matplotlib.pyplot
import tensorflow
import pandas

class train(Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)

    def init(self, timeStamp=0.0):
        self.services.stage_state()

        if timeStamp == 0.0:
            self.services.stage_input_files('model_config.json')
            self.config = adaptive.load_json('model_config.json')
            self.trainer = adaptive.adaptive_train.new_model(self.config,
                                                             10, 10, 'tanh',
                                                             0.0, 0.0, None, 'unconstrained')
            self.validation_data = adaptive.validation(None, self.config)

        if not os.path.exists('training_data.json'):
            os.rename('new_data.json', 'training_data.json')

        training_data = adaptive.load_json('training_data.json')

        if os.path.exists('new_data.json'):
            new_data = adaptive.load_json('new_data.json')

            for key in training_data:
                training_data[key] += new_data[key]

        self.trainer.set_inital_data(training_data)

    def step(self, timeStamp=0.0):
        workers = multiprocessing.cpu_count()

        self.trainer.train(10, 1000, workers, False, 0.0, self.validation_data, 1.0E-10)
        self.trainer.save_model('saved_model')

        self.trainer.create_prediction_data(1000)

        self.trainer.set_parameter_covariance_matrix()
        self.trainer.set_model_covariance_matrix()

        self.trainer.create_suplimental_data(10, 0.1, 2)
        self.trainer.save_suplimental_data('new_data.json')

        self.services.update_state()
        plot_model(self.trainer, self.config)

def denormalize(x, ranges):
    return adaptive.denormalize(x, ranges['upper_range'], ranges['lower_range'])

def plot_model(trainer, config):
    x_pred = tensorflow.reshape(denormalize(trainer.prediction_input,
                                            config['inputs'][0]),
                                (trainer.prediction_input.shape[0],))
    y_pred = tensorflow.reshape(denormalize(trainer.model_prediction,
                                            config['outputs'][0]),
                                (trainer.prediction_input.shape[0],))
    yp_pred = tensorflow.reshape(denormalize(trainer.model_prediction + trainer.model_prediction_sigma,
                                             config['outputs'][0]),
                                 (trainer.prediction_input.shape[0],))
    ym_pred = tensorflow.reshape(denormalize(trainer.model_prediction - trainer.model_prediction_sigma,
                                             config['outputs'][0]),
                                 (trainer.prediction_input.shape[0],))

    data = pandas.DataFrame()
    data['x'] = x_pred
    data['y'] = y_pred
    data['y+'] = yp_pred
    data['y-'] = ym_pred

    data.sort_values('x', inplace=True)

    matplotlib.pyplot.clf()
    matplotlib.pyplot.fill_between(data['x'], data['y+'], data['y-'])
    matplotlib.pyplot.plot(data['x'], data['y'], color='black')
    matplotlib.pyplot.scatter(denormalize(trainer.training_inputs,
                                          config['inputs'][0]),
                              denormalize(trainer.training_outputs,
                                          config['outputs'][0]))

    matplotlib.pyplot.pause(0.05)
