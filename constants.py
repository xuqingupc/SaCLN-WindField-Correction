import os

def get_dir(directory):
    """
    Creates the given directory if it does not exist.
    @param directory: The path to the directory.
    @return: The path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

save_name = ('SaCLN_Wind')
save_dir = '../save/'
train_save_dir = get_dir(os.path.join(save_dir, 'train/', save_name))
test_save_dir = get_dir(os.path.join(save_dir, 'test/', save_name))
save_models_dir = get_dir(os.path.join(save_dir, 'models/', save_name))
loss_save_dir = get_dir(os.path.join(save_dir,'loss/', save_name))

train_original_dir = "/train/Forecast/"
train_revised_dir = "/train/Reanalysis/"
test_original_dir = "/test/Forecast/"
test_revised_dir = "/test/Reanalysis/"

data_height = 81  #121
data_width = 81   #121
