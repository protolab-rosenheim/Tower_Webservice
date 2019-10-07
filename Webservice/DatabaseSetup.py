from Webservice.DbModels import Module, Slot


class DatabaseSetup:
    def __init__(self, db, config):
        self.db = db
        self.config = config

    def setup_modules(self):
        """
        Sets up the modules and slots specified in the config objects and adds them to the database if they do not
        exist already
        """
        if self.modules_do_not_exist():
            modules = self.create_modules_from_config(self.config['modules'])
            self.db.session.add_all(modules)
            self.db.session.commit()

    def modules_do_not_exist(self):
        return not self.db.session.query(Module).count()

    def create_modules_from_config(self, modules_config):
        """
        Creates modules and slots specified in the modules_config
        """
        modules = []
        for module_in_config in modules_config:
            module_number = module_in_config['module_number']
            module = Module(module_number=module_number, slots=[])

            if 'slots' in module_in_config:
                slots = self.create_slots_from_config(module_number, module_in_config['slots'])
                module.slots.extend(slots)
            modules.append(module)
        return modules

    def create_slots_from_config(self, module_number, slots_config):
        slots = []
        for slot_in_config in slots_config:
            slots.append(Slot(module_id=module_number, slot_name=slot_in_config['slot_name']))
        return slots
