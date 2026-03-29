from odoo import models, fields


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    total_cost = fields.Float(string='Total Cost', readonly=True)

    # We bring this field in strictly to rename its label in the UI
    product_tmpl_id = fields.Many2one('product.template', string='Main Product', readonly=True)

    def _select(self):
        # We append the raw field without SUM(), letting the Pivot view handle the math
        return super()._select() + ", l.total_cost AS total_cost"