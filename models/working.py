from odoo import fields, models, api, _


class Working(models.Model):
    _name = "working"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "People are working"
    # _inherit = 'sale.order.line'

    name = fields.Char(string="Service")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    origin = fields.Many2one('sale.order', string="Source Document")
    sale_order_line_id = fields.Many2one('sale.order')
    partner_id = fields.Many2one('res.partner')
    parent_name = fields.Char(related='partner_id.name', string="Name")
    parent_address = fields.Text(string="Address")
    phone = fields.Char(related='partner_id.phone', string="Phone")
    assign = fields.Many2one(string="Assign")
    state_working = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting'),
        ('assigned', 'Ready'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string="Status")

    note = fields.Text(string="Note")
    # sale_id = fields.Many2one(related='group_id.sale.order')
    sale_id = fields.Many2one('sale.order')

    completed_work = fields.Selection([
        ('incomplete', 'Incomplete'),
        ('completed', 'Completed')
    ], string="Completed", default=False)

    def action_cancel(self):
        print("Cancel")

    def action_completed(self):
        print("Completed")


