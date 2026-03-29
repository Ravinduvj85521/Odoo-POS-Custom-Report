# POS Custom Reports (Odoo 19)

A lightweight custom Odoo 19 module that enhances the Point of Sale (POS) Orders Analysis report by exposing critical financial metrics and streamlined grouping options.

## 📝 Description

By default, Odoo's POS Orders Analysis report groups sales strictly by individual product variants (e.g., specific sizes and colors) and hides raw cost data. For apparel and retail brands, this creates cluttered reports that make it difficult to evaluate the overall performance of a product line.

This module solves that problem by making two key adjustments to the `report.pos.order` view:
1. **Unlocks Template Grouping:** It exposes Odoo's native `product_tmpl_id` in the advanced search view, renamed as **Main Product**. This allows users to cleanly roll up all variant sales (sizes, colors) into a single, easy-to-read row for the parent item.
2. **Injects Cost Tracking:** It extends the underlying SQL query to pull `l.total_cost` directly into the Pivot and Graph views, allowing users to track the **Total Cost** measure alongside standard metrics like Total Price and Margin.

## ✨ Features

* **Total Cost Measure:** Injects `Total Cost` directly into the Measures dropdown.
* **Main Product Grouping:** Exposes the "Main Product" (Template) grouping option in the advanced search filters.

## 🛠️ Technical Specifications

* **Odoo Version:** 19.0 (Community Edition)
* **Dependencies:** `point_of_sale`
* **Technical Name:** `pos_report`

## 🚀 Installation

1. Clone or download this repository.
2. Place the `pos_report` folder into your Odoo `custom_addons` directory.
3. Restart your Odoo server service.
4. Log into Odoo as an Administrator and activate **Developer Mode**.
5. Navigate to the **Apps** menu and click **Update Apps List**.
6. Remove the `Apps` filter in the search bar, search for `POS Custom Reports`, and click **Activate**.

## 👨‍💻 Author

* **Ravinduvj85521**
