from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DbModelExtension(db.Model):
    __abstract__ = True

    def to_dict(self):
        tmp_dict = self.__dict__
        ret_dict = {}
        for key in self.__table__.columns.keys():
            if key in tmp_dict:
                if tmp_dict[key].__class__.__name__ == 'datetime':
                    ret_dict[key] = tmp_dict[key].isoformat()
                else:
                    ret_dict[key] = tmp_dict[key]
        return ret_dict

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.to_dict() == other.to_dict():
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Module(DbModelExtension):
    module_number = db.Column(db.Integer, primary_key=True)
    slots = db.relationship("Slot")


class Slot(DbModelExtension):
    id = db.Column(db.Integer, primary_key=True)
    slot_name = db.Column(db.String)
    module_id = db.Column(db.Integer, db.ForeignKey('module.module_number'))
    coating = db.relationship("Coating", uselist=False, backref="slot")


class Coating(DbModelExtension):
    name = db.Column(db.String, primary_key=True)
    slot_id = db.Column(db.Integer, db.ForeignKey('slot.id'), unique=True)
    text_short = db.Column(db.String)
    article_id = db.Column(db.String)
    order_id = db.Column(db.String)
    supplier = db.Column(db.String)
    photo = db.Column(db.String)
    sweight = db.Column(db.Numeric)
    description = db.Column(db.String)
