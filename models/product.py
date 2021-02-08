from odoo import models, fields, api, _


class Product(models.Model):
    _inherit = "product.template"

    work_ok = fields.Boolean(string='Can be Work', default=True)




