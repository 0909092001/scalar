import nbformat
from nbclient import NotebookClient

nb_path = "student_dropout_system.ipynb"
out_path = "executed.ipynb"

nb = nbformat.read(nb_path, as_version=4)

# Choose kernel from notebook metadata if present, otherwise default to 'python3'
kernel_name = None
try:
	ks = nb.metadata.get("kernelspec", {})
	kernel_name = ks.get("name") or ks.get("display_name")
except Exception:
	kernel_name = None
if not kernel_name:
	kernel_name = "python3"

client = NotebookClient(nb, timeout=600, kernel_name=kernel_name)
client.execute()
nbformat.write(nb, out_path)
print(f"Executed and saved -> {out_path}")
