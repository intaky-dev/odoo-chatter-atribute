from odoo import models, fields

class ProductAttribute(models.Model):
    _inherit = 'product.attribute'  # Inherit the existing model
    _mail_thread = True  # Enable mail.thread features
    _mail_activity_mixin = True  # Enable mail.activity.mixin features

    name = fields.Char(
        tracking=True  # Add tracking to the 'name' field
    )
    display_type = fields.Selection(
        selection_add=[],
        tracking=True  # Add tracking to the 'display_type' field
    )