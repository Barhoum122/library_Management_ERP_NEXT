# Copyright (c) 2026, faris@example.com and contributors
# For license information, please see license.txt
import frappe # type: ignore
from frappe.model.document import Document # type: ignore


class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
		frappe.msgprint((f"أهلاً بك {self.full_name}، تم إعداد بيانات العضوية بنجاح."),);
	pass
