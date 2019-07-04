def to_json(obj):
        dict_json = {}
        for field in dir(obj):
            if not field.startswith('_'):
                dict_json.update({field:str(getattr(obj,field))})
        return dict_json