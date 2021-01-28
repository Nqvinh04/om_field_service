from odoo import fields, models, api, _


class Working(models.Model):
    _name = "working"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "People are working"
    # _inherit = 'sale.order.line'

    name = fields.Char(string="Name")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    origin = fields.Many2one(string="Source Document")

    parent_name = fields.Many2one(string="Name")
    parent_address = fields.Many2one(string="Address")
    phone = fields.Many2one(string="Phone")
    assign_id = fields.Many2one(string="Assign")
    # state = fields.Selection([
    #     ('draft', 'Draft'),
    #     ('waiting', 'Waiting Another Operation'),
    #     ('confirmed', 'Waiting'),
    #     ('assigned', 'Ready'),
    #     ('done', 'Done'),
    #     ('cancel', 'Cancelled'),
    # ], string="Status")


