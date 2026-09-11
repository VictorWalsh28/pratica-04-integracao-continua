resource "local_file" "exemplo" {
  filename = var.file_name
  content  = var.file_content
}
