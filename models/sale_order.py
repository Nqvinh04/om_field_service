from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.template')
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
            'partner_id': self.partner_id.id,
            'origin': self.name,
            # 'assign': self.order_line.assign_id,
            # 'sale_order_line_id': self.order_line.id,
        })



