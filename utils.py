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


def convert_synetune_dict_to_LLAMBO_df(synetune_dict):
    if isinstance(synetune_dict, dict):
        synetune_dict = [synetune_dict]

    op_0_to_1 = []
    op_0_to_2 = []
    op_0_to_3 = []
    op_1_to_2 = []
    op_1_to_3 = []
    op_2_to_3 = []

    for item in synetune_dict:
        op_0_to_1.append(item['hp_x0'])
        op_0_to_2.append(item['hp_x1'])
        op_0_to_3.append(item['hp_x2'])
        op_1_to_2.append(item['hp_x3'])
        op_1_to_3.append(item['hp_x4'])
        op_2_to_3.append(item['hp_x5'])

    data = {
        'op_0_to_1': op_0_to_1,
        'op_0_to_2': op_0_to_2,
        'op_0_to_3': op_0_to_3,
        'op_1_to_2': op_1_to_2,
        'op_1_to_3': op_1_to_3,
        'op_2_to_3': op_2_to_3
    }

    df = pd.DataFrame(data)
    return df
