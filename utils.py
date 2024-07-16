def convert_LLAMBO_df_to_synetune_dict(config):
    config = config.to_dict()
    dicts = []
    length = len(config['op_0_to_1'])
    for i in range(length):
        original_dict = {
            'hp_x0': config['op_0_to_1'][i],
            'hp_x1': config['op_0_to_2'][i],
            'hp_x2': config['op_0_to_3'][i],
            'hp_x3': config['op_1_to_2'][i],
            'hp_x4': config['op_1_to_3'][i],
            'hp_x5': config['op_2_to_3'][i]
        }
        if length == 1:
            return original_dict
        dicts.append(original_dict)

    return dicts
