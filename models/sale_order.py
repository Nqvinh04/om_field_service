from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.template')
    working_ids = fields.One2many('working', 'sale_id', string='Working')
    working_count = fields.Integer(string="Working Orders", compute='_compute_working_ids')

    def action_view_work(self):
        print("thanh Cong")

    @api.depends('working_ids')
    def _compute_working_ids(self):
        for order in self:
            order.working_count = len(order.working_ids)


    def action_confirm(self):
        for rec in self.order_line:
            if rec.type == 'service' and rec.working_ok == True:
                super(SaleOrder, self).action_confirm()
                if rec.assign_id.id != self.working_ids.assign.id:
                    self.env['working'].create({
                        'partner_id': self.partner_id.id,
                        'origin': self.name,
                        'assign': rec.assign_id.id,
                        'sale_order_line_id': rec,
                        'sale_id': self.id,
                    })

            else:
                print('ko tao moi')
                raise ValidationError(_('Sản phẩm "%s" chưa sẵn sàng', rec.product_id.name))

            # else:
            #     self.working_ok_notification()
