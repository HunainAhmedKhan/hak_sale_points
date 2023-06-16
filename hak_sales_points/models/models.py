# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateInh(models.Model):
    _inherit = 'product.template'

    sale_point = fields.Integer(string="Sales Point")


class PosOrderInh(models.Model):
    _inherit = 'pos.order'

    total_sale_point = fields.Integer(compute='compute_total_sale_point', store=True)

    @api.depends('lines.product_id')
    def compute_total_sale_point(self):
        points = 0
        for rec in self.lines:
            points += rec.product_id.sale_point * rec.qty
        self.total_sale_point = points


class PosOrderReportInh(models.Model):
    _inherit = "report.pos.order"

    total_sale_point = fields.Integer(string="Total Sale Points")

    def _select(self):
        return super(PosOrderReportInh, self)._select() + ',s.total_sale_point AS total_sale_point'

    def _group_by(self):
        return super(PosOrderReportInh, self)._group_by() + ',s.total_sale_point'
