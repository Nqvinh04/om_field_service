from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    working_count = fields.Integer(string="Working Orders")

    def action_view_work(self):
        print("thanh Cong")

