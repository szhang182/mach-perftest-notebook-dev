def flat(data, parent_dir):
    '''
    Convert JSON data to a dictionary.
    
    :param list/dict data : json data.
    :param list parent_dir: json fields. 
    
    :return dict: {subtest:json_value}
    '''
    def recursive_helper(data, parent_dir, ret):
        if isinstance(data, list):
            for item in data:
                ret.update(recursive_helper(item, parent_dir, ret))
        elif isinstance(data, dict):
            for k, v in data.items():
                current_dir = parent_dir.copy()
                current_dir.append(k)
                subtest = '.'.join(current_dir)
                if (isinstance(v, dict) and v.values()) or isinstance(v, list):
                    ret.update(recursive_helper(v, current_dir, ret))
                elif v:
                    existed_data = ret.get(subtest)
                    if existed_data:
                        existed_data.append(v)
                        ret.update({subtest: existed_data})
                    else:
                        ret.update({subtest: [v]})

        return ret

    return recursive_helper(data, parent_dir, {})
