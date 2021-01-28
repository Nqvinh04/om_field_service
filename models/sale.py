from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    assign_id = fields.Many2one('res.partner', string='Assign')
    type = fields.Selection(related='product_id.type', string="Type")















