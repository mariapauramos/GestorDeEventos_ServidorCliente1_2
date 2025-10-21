using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace POCClienteEvento
{
    public partial class GUIEliminarED : Form
    {
        public GUIEliminarED()
        {
            InitializeComponent();
        }

        private void buttonCerrar_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private async void buttonBuscar_Click(object sender, EventArgs e)
        {
            try
            {
                // Obtener el id ingresado
                string idEvento = txtIdEvento.Text.Trim();
                if (string.IsNullOrEmpty(idEvento))
                {
                    MessageBox.Show("Por favor ingresa un IdEvento.");
                    return;
                }

                using (HttpClient client = new HttpClient())
                {
                    // Autenticación
                    var credentials = Convert.ToBase64String(System.Text.Encoding.ASCII.GetBytes("admin:admin"));
                    client.DefaultRequestHeaders.Authorization =
                        new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", credentials);

                    // URL con el ID
                    string url = $"http://localhost:8091/eventos/{idEvento}";

                    //Request GET
                    HttpResponseMessage response = await client.GetAsync(url);

                    if (response.IsSuccessStatusCode)
                    {
                        string json = await response.Content.ReadAsStringAsync();

                        using (JsonDocument doc = JsonDocument.Parse(json))
                        {
                            var item = doc.RootElement;

                            // Obtener informacion
                            string nombre = item.GetProperty("nombre").GetString();
                            string ciudad = item.GetProperty("ciudad").GetString();
                            int asistentes = item.GetProperty("asistentes").GetInt32();
                            string fecha = item.GetProperty("fecha").GetString();
                            double valorEntrada = item.GetProperty("valorEntrada").GetDouble();
                            string tipoDeporte = item.TryGetProperty("tipoDeporte", out var deporteProp)
                                ? deporteProp.GetString()
                                : "";

                            // Asignar a los txt
                            txtNombre.Text = nombre;
                            txtCiudad.Text = ciudad;
                            txtAsistentes.Text = asistentes.ToString();
                            txtFecha.Text = fecha;
                            txtValorEntrada.Text = valorEntrada.ToString("N2");
                            txtTipoDeporte.Text = tipoDeporte;
                        }
                        txtNombre.ReadOnly = true;
                        txtCiudad.ReadOnly = true;
                        txtAsistentes.ReadOnly = true;
                        txtValorEntrada.ReadOnly = true;
                        txtTipoDeporte.ReadOnly = true;
                        txtFecha.ReadOnly = true;
                    }
                    else
                    {
                        MessageBox.Show($"No se encontró el evento con el Id {idEvento}");
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error al buscar evento: " + ex.Message);
            }

        }

        private async void buttonEliminar_Click(object sender, EventArgs e)
        {
            try
            {
                string idEvento = txtIdEvento.Text.Trim();
                if (string.IsNullOrEmpty(idEvento))
                {
                    MessageBox.Show("Primero busca y selecciona un IdEvento para eliminar.");
                    return;
                }

                // Confirmación antes de eliminar
                var confirm = MessageBox.Show($"¿Estás seguro de eliminar el evento con el siguiente Id: {idEvento}?",
                    "Confirmar eliminación", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);

                if (confirm == DialogResult.No) return;

                using (HttpClient client = new HttpClient())
                {
                    var credentials = Convert.ToBase64String(Encoding.ASCII.GetBytes("admin:admin"));
                    client.DefaultRequestHeaders.Authorization =
                        new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", credentials);

                    string url = $"http://localhost:8091/eventos/{idEvento}";

                    HttpResponseMessage response = await client.DeleteAsync(url);

                    if (response.IsSuccessStatusCode)
                    {
                        string result = await response.Content.ReadAsStringAsync();
                        MessageBox.Show(result, "Evento Eliminado", MessageBoxButtons.OK, MessageBoxIcon.Information);

                        // Limpiar campos después de eliminar
                        txtIdEvento.Clear();
                        txtNombre.Clear();
                        txtCiudad.Clear();
                        txtAsistentes.Clear();
                        txtFecha.Clear();
                        txtValorEntrada.Clear();
                        txtTipoDeporte.Clear();
                    }
                    else
                    {
                        string errorMsg = await response.Content.ReadAsStringAsync();
                        MessageBox.Show($"Error al eliminar: {errorMsg}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error al eliminar evento: " + ex.Message);
            }

        }
    }
}
