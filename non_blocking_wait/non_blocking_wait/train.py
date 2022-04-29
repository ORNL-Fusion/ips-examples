import adaptive
import multiprocessing
import os

class train(Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)

    def init(self, timeStamp=0.0):
        self.services.stage_state()

        if timeStamp == 0.0:
            self.services.stage_input_files('model_config.json')
            config = adaptive.load_json('model_config.json')
            self.trainer = adaptive.adaptive_train.new_model(config,
                                                             10, 10, 'tanh',
                                                             0.0, 0.0, None, 'unconstrained')

        if !os.path.exists('training_data.json'):
            os.rename('new_data.json', 'training_data.json')

        training_data = adaptive.load_json('training_data.json')

        if os.path.exists('new_data.json')
            new_data = adaptive.load_json('new_data.json')

            for key in self.training_data:
                training_data[key] += new_data[key]

        self.trainer.set_inital_data(training_data)

    def step(self, timeStamp=0.0):
        workers = multiprocessing.cpu_count()

        self.trainer.train(10,
                           1000,
                           workers)
        self.trainer.save_model('saved_model')

        trainer.create_prediction_data(1000)

        trainer.set_parameter_covariance_matrix()
        trainer.set_model_covariance_matrix()

        trainer.save_prediction_data('new_data.json')
        trainer.save_covariance_matrix('param_covar_matrix.json')

        self.services.update_state()
