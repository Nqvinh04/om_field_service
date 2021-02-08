from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    assign_id = fields.Many2one('hr.employee', string='Assign')
    type = fields.Selection(related='product_id.type', string="Type")
    working_ok = fields.Boolean(related='product_id.work_ok')
    working_id = fields.Many2one('working')
    state_working = fields.Selection(related='working_id.state_working', string="Status")



















