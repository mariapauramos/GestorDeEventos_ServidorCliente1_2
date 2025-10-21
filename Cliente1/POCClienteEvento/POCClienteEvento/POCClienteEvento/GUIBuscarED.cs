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
    public partial class GUIBuscarED : Form
    {
        public GUIBuscarED()
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

                    // Petición GET
                    HttpResponseMessage response = await client.GetAsync(url);

                    if (response.IsSuccessStatusCode)
                    {
                        string json = await response.Content.ReadAsStringAsync();

                        using (JsonDocument doc = JsonDocument.Parse(json))
                        {
                            var item = doc.RootElement;

                            
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
    }
}
