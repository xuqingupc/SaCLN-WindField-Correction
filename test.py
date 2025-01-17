import numpy as np
import tensorflow as tf
from model import WindFieldCorrection
import constants as c
from utils import read_data


def load_data(test_dir, batch_size, histlen, futulen):
    test_files_original = np.array(glob.glob(os.path.join(test_dir, '*.npy')))
    test_files_original.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

    data = read_data(test_files_original, batch_size, histlen, futulen)
    return data


def test_model(sess, model, test_data, histlen):
    test_original = test_data[:, :histlen + 1, :, :, :]
    test_revised = test_data[:, histlen + 1:, :, :, :]

    test_revised_fake = model.sess.run(model.test_revised_fake,
                                       feed_dict={model.test_original: test_original, model.test_revised: test_revised})

    test_revised_fake = np.array(test_revised_fake)
    test_diff = np.mean(np.abs(test_revised - test_revised_fake))  # 绝对平均误差 MAE

    print("Test error: ", test_diff)


if __name__ == '__main__':
    # Set up the session and model
    sess = tf.compat.v1.Session()
    model = WindFieldCorrection(sess=sess,
                                train_batch_size=4,
                                test_batch_size=1,
                                epochs=1,
                                checkpoint_file='WindPred10.ckpt',
                                lambdl1=5,
                                save_freq=1,
                                histlen=2,
                                futulen=1,
                                learn_rate=5e-8)

    # Load test data
    test_data = load_data(c.test_original_dir, 1, model.histlen, model.futulen)

    # Build and initialize the model
    model.build_model()
    saver = tf.compat.v1.train.Saver()
    saver.restore(sess, tf.train.latest_checkpoint(c.save_models_dir))
    print("Model restored.")

    # Test the model
    test_model(sess, model, test_data, model.histlen)