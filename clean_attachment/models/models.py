from odoo import models, fields
from odoo.exceptions import UserError

class CleanAttachmentWizard(models.TransientModel):
    _name = 'clean.attachment.wizard'
    _description = 'Wizard to Clean Attachments'

    model_id = fields.Many2one(comodel_name='ir.model', string='Model', required=True)
    from_date = fields.Date("From Date")
    to_date = fields.Date("To Date")
    file_type = fields.Selection(
        selection=[
            ('pdf', 'PDF'),
            ('jpeg_image', 'JPEG Image'),
            ('csv', 'CSV'),
        ],
        default='pdf', required=True
    )

    def clean_attachments(self):
        """Deletes attachments based on selected model, file type, and date filters."""
        mimetype_mapping = {
            'pdf': 'application/pdf',
            'jpeg_image': 'image/jpeg',
            'csv': 'text/csv',
        }
        mimetype = mimetype_mapping.get(self.file_type)

        model_name = self.model_id.model

        # Fetch only record IDs instead of full records to optimize memory usage
        model_ids = self.env[model_name].search([]).ids

        if not model_ids:
            raise UserError(f"No records found for model '{model_name}'. No attachments to clean!")

        # Define domain for attachment search
        domain = [
            ('mimetype', '=', mimetype),
            ('res_id', 'in', model_ids),
            ('res_model', '=', model_name),
        ]

        # Apply date filters if provided
        if self.from_date:
            domain.append(('create_date', '>=', self.from_date))
        if self.to_date:
            domain.append(('create_date', '<=', self.to_date))

        # Check if any attachments match the criteria before deleting
        attachment_count = self.env['ir.attachment'].search_count(domain)
        if attachment_count == 0:
            raise UserError(f"No attachments of type '{self.file_type.upper().replace('_',' ')}' found for the selected criteria!")

        # Bulk delete attachments
        self.env['ir.attachment'].search(domain).unlink()

        return {'type': 'ir.actions.act_window_close'}