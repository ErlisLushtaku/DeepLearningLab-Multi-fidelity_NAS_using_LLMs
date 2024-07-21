import pandas as pd


def convert_LLAMBO_df_to_synetune_dict(config):
    config = config.to_dict()
    dicts = []
    length = len(config['op_0_to_1'])
    if length == 1:
        key = list(config['op_0_to_1'].keys())[0]
        original_dict = {
            'hp_x0': config['op_0_to_1'][key],
            'hp_x1': config['op_0_to_2'][key],
            'hp_x2': config['op_0_to_3'][key],
            'hp_x3': config['op_1_to_2'][key],
            'hp_x4': config['op_1_to_3'][key],
            'hp_x5': config['op_2_to_3'][key]
        }
        return original_dict
    else:
        for i in range(length):
            original_dict = {
                'hp_x0': config['op_0_to_1'][i],
                'hp_x1': config['op_0_to_2'][i],
                'hp_x2': config['op_0_to_3'][i],
                'hp_x3': config['op_1_to_2'][i],
                'hp_x4': config['op_1_to_3'][i],
                'hp_x5': config['op_2_to_3'][i]
            }
            dicts.append(original_dict)

    return dicts


import pandas as pd

def convert_synetune_dict_to_LLAMBO_compatible_format(synetune_dicts):
    # Check if input is a list of dictionaries
    if isinstance(synetune_dicts, list):
        data_list = []
        for synetune_dict in synetune_dicts:
            data = {
                'op_0_to_1': synetune_dict['hp_x0'],
                'op_0_to_2': synetune_dict['hp_x1'],
                'op_0_to_3': synetune_dict['hp_x2'],
                'op_1_to_2': synetune_dict['hp_x3'],
                'op_1_to_3': synetune_dict['hp_x4'],
                'op_2_to_3': synetune_dict['hp_x5']
            }
            data_list.append(data)
        # Convert the list of dictionaries to a DataFrame
        return pd.DataFrame(data_list)
    else:
        # Process a single dictionary as before
        data = {
            'op_0_to_1': synetune_dicts['hp_x0'],
            'op_0_to_2': synetune_dicts['hp_x1'],
            'op_0_to_3': synetune_dicts['hp_x2'],
            'op_1_to_2': synetune_dicts['hp_x3'],
            'op_1_to_3': synetune_dicts['hp_x4'],
            'op_2_to_3': synetune_dicts['hp_x5']
        }
        # Convert the dictionary to a DataFrame
        return data