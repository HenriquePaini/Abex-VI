class FormularioRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'formulario':
            return 'formulario_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'formulario':
            return 'formulario_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'formulario':
            return db == 'formulario_db'
        return None
