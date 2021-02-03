from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one('res.partner')
    working_ids = fields.One2many('working', 'sale_id', string='Working')
    working_count = fields.Integer(string="Working Orders", computed='_compute_working_ids')

    def action_view_work(self):
        print("thanh Cong")

    @api.depends('working_ids')
    def _compute_working_ids(self):
        for order in self:
            order.working_count = len(order.working_ids)


    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        self.env['working'].create({
            'name': self.partner_id.name,
            'origin': self.origin,
            'parent_name': self.partner_id.name,
            'phone': self.partner_id.phone,
            # 'assign': self.assign_id,
        })








