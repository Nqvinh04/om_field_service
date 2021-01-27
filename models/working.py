from odoo import fields, models, api, _


class Working(models.Model):
    _name = "working"
    _description = "People are working"
    # _inherit = 'sale.order.line'

    name = fields.Char(string="Name")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")

    # invoice_lines = fields.Many2many('sale.order.line', 'working_invoice_lines', 'working_id',
    #                                  'invoice_line_id', string='Invoice lines')

