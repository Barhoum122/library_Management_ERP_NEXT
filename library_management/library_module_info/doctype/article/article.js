// Copyright (c) 2026, faris@example.com and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Article", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Article", {
    refresh(frm) {
       
        frm.add_custom_button(__('Post'), function() {
           frappe.msgprint(__('Succes Posted!!'));
         
        });
    }
});
