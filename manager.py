class Manager:
    def __init__(self, _class):
        self._class = _class

    def __str__(self):
        return f'manager: {self._class}'

    def search(self, **kwargs):

        results = list()
        set_min = set()
        set_max = set()

        for key, value in kwargs.items():

            if key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            else:
                compare_key = 'equal'

            for obj in self._class.objects_list:

                if hasattr(obj, key):

                    if compare_key == 'min':
                        if getattr(obj, key) >= value:
                            set_min.add(obj)
                            results.append(obj)

                    if compare_key == 'max':
                        if getattr(obj, key) <= value:
                            set_max.add(obj)
                            results.append(obj)

                    if compare_key == 'equal':
                        if getattr(obj, key) == value:
                            results.append(obj)

        if len(kwargs.keys()) == 2:

            print(f'min : {set_max}')
            print(f'max : {set_min}')
            return f'result : {set_min & set_max}'

        return results

    def count(self):
        return len(self._class.objects_list)
