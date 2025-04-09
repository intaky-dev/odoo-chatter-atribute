from odoo import models, fields

class ProductAttribute(models.Model):
    _inherit = ['product.attribute', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        track_visibility='onchange'
    )
    display_type = fields.Selection(
        selection_add=[],
        track_visibility='onchange'
    )
