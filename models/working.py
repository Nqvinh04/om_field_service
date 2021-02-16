from odoo import fields, models, api, _
from odoo.exceptions import UserError


class Working(models.Model):
    _name = "working"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "People are working"
    # _inherit = 'sale.order.line'

    name = fields.Char(string="Working ID", copy=False, readonly=True, index=True, default=lambda self: _('New'))
    # name_seq = fields.Char(string='Working ID', copy=False, readonly=True, index=True, default=lambda self: _('New'))
    start_time = fields.Datetime(string="Start Time", default=fields.Datetime.now, inverse='')
    end_time = fields.Datetime(string="End Time")
    origin = fields.Char(string="Source Document", index=True)
    sale_order_line_id = fields.One2many('sale.order.line', 'working_id', string="Sale Order Line")
    partner_id = fields.Many2one('res.partner', string="Name")
    # parent_name = fields.Many2one('partner_id.name', string="Name")
    partner_address = fields.Text(string="Address")
    partner_phone = fields.Char(string="Phone", related='partner_id.phone')
    # assign = fields.Many2one('hr.employee', string="Assign", related='sale_order_line_id.assign_id')
    assign = fields.Many2one('hr.employee', string="Assign")
    state_working = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirm'),
        # ('completed', 'Completed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string="Status", readonly=True, default='draft')

    note = fields.Text(string='Notes')
    # sale_order_id = fields.Many2one('sale.order')
    sale_id = fields.Many2one('sale.order', string="Sales Order")

    show_get_job = fields.Boolean(computed='_compute_show_get_job')
    # show_get_job = fields.Boolean(default=True)
    # show_check_availability = fields.Boolean(computed='_compute_show_check_availability')
    # show_completed = fields.Boolean(computed='_compute_show_completed')
    show_completed = fields.Boolean(default=True)

    completed_work = fields.Selection([
        ('incomplete', 'Incomplete'),
        ('completed', 'Completed')
    ], string="Completed", default=False)

    def action_confirm(self):
        print("action")
        print(self.show_get_job)
        for rec in self:
            rec.state_working = 'confirmed'
            print(rec.show_get_job)
        print(self._compute_show_get_job())
    print(show_get_job)

    # def action_check_availability(self):
    #     print("check_availability")

    def action_completed(self):
        print("Completed")
        print(self.show_completed)
        for rec in self:
            rec.state_working = 'done'
            # rec.write_working()
        print(self._compute_show_completed())

    # def write_working(self):
    #     self.env['working'].write({
    #         'end_time': fields.Datetime.now,
    #     })

    # def write_working(self, vals):
    #     result = super(Working, self).write(vals)
    #     self.env['working'].write({
    #         'end_time': fields.Datetime.now,
    #     })
    #     return result

    # def action_done(self):
    #     print("Done")
    #     for rec in self:
    #         rec.state_working = 'done'

    def action_cancel(self):
        print("Cancel")
        for rec in self:
            rec.state_working = 'cancel'

    # @api.depends('state_working', 'sale_order_line_id')
    # def _compute_show_check_availability(self):
    #     print("show_check_availability")

    @api.depends('state_working', 'sale_order_line_id')
    # @api.onchange('state_working')
    def _compute_show_completed(self):
        print("show_completed")
        for working in self:
            if working.state_working != 'done':
                working.show_completed = False
            else:
                working.show_completed = True
            print(self.show_completed)



    @api.depends('state_working', 'sale_order_line_id')
    def _compute_show_get_job(self):
        print("Hoạt động")
        for working in self:
            if working.state_working != 'draft':
                working.show_get_job = False
            else:
                working.show_get_job = True
        print(self.show_get_job)

    # @api.depends('sale_order_line_id.state', 'sale_order_line_id.working_id')
    # def _compute_state_working(self):
    #     for working in self:
    #         if working.sale_order_line_id:
    #             working.state_working == 'draft'

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
