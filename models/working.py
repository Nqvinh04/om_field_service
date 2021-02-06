from odoo import fields, models, api, _
from odoo.exceptions import UserError


class Working(models.Model):
    _name = "working"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "People are working"
    # _inherit = 'sale.order.line'

    name = fields.Char(string=" Service", copy=False, readonly=True, index=True, default=lambda self: _('New'))
    # name_seq = fields.Char(string='Working ID', copy=False, readonly=True, index=True, default=lambda self: _('New'))
    start_time = fields.Datetime(string="Start Time", default=fields.Datetime.now, inverse='')
    end_time = fields.Datetime(string="End Time")
    origin = fields.Many2one('sale.order', string="Source Document")
    sale_order_line_id = fields.Many2one('sale.order.line')
    partner_id = fields.Many2one('res.partner', string="Name")
    # parent_name = fields.Many2one('partner_id.name', string="Name")
    partner_address = fields.Text(string="Address")
    partner_phone = fields.Char(string="Phone", related='partner_id.phone')
    assign = fields.Many2one('hr.employee', string="Assign")
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

    def _set_start_time(self):
        for working in self:
            if working.state_working in ('done', 'cancel'):
                raise UserError(_("You cannot change the Scheduled Date on a done or cancelled transfer."))
            # working.move_lines.write({'date': working.start_time})

    @api.model
    def create(self, vals):
        if vals.get('name', _('new')) == _('new'):
            vals['name'] = self.env['ir.sequence'].next_by_code('working.sequence') or _('new')
        result = super(Working, self).create(vals)
        return result


