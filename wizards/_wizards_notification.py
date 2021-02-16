from odoo import models, fields, api, _


class WizardsNotification(models.TransientModel):
    _name = 'wizards.notification'

    product_id = fields.Many2one('product.template')
    message = fields.Text('Message')

    def action_ok(self):
        """ close wizard"""
        return {
            'type': 'ir.action.act_window_close'
        }
