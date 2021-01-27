from odoo import models, fields, api, _


# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#     _inherits = {'res.users': 'users_id'}
#
#     assign_id = fields.Many2one('res.users', string="Assign")

class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    assign_id = fields.Many2one('res.partner', string='Assign')
    type = fields.Selection(related='product_id.type', string="Type", )















