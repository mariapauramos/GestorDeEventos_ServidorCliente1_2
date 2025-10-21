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
    public partial class GUIListarParametroED : Form
    {
        public GUIListarParametroED()
        {
            InitializeComponent();
        }

        private void buttonCerrar_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private async void buttonListar_Click(object sender, EventArgs e)
        {
            try
    {
                using (HttpClient client = new HttpClient())
                {
                    // Autenticación
                    var credentials = Convert.ToBase64String(Encoding.ASCII.GetBytes("admin:admin"));
                    client.DefaultRequestHeaders.Authorization =
                        new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", credentials);

                    // Capturar parámetros
                    string ciudad = txtCiudad.Text.Trim();
                    string tipoDeporte = txtTipoDeporte.Text.Trim();

                    // Construir URL con query y parametros
                    string url = "http://localhost:8091/eventos/filtroED";
                    List<string> queryParams = new List<string>();
                    if (!string.IsNullOrEmpty(ciudad))
                        queryParams.Add($"ciudad={ciudad}");
                    if (!string.IsNullOrEmpty(tipoDeporte))
                        queryParams.Add($"tipoDeporte={tipoDeporte}");

                    if (queryParams.Any())
                        url += "?" + string.Join("&", queryParams);

                    // Petición GET
                    HttpResponseMessage response = await client.GetAsync(url);

                    if (response.IsSuccessStatusCode)
                    {
                        var json = await response.Content.ReadAsStringAsync();

                        using (JsonDocument doc = JsonDocument.Parse(json))
                        {
                            var eventos = new List<object>();

                            foreach (var item in doc.RootElement.EnumerateArray())
                            {
                                string idEvento = item.GetProperty("idEvento").GetString();
                                string nombre = item.GetProperty("nombre").GetString();
                                string ciudadResp = item.GetProperty("ciudad").GetString();
                                int asistentes = item.GetProperty("asistentes").GetInt32();
                                string fecha = item.GetProperty("fecha").GetString();
                                double valorEntrada = item.GetProperty("valorEntrada").GetDouble();
                                string tipoDeporteResp = item.TryGetProperty("tipoDeporte", out var deporteProp)
                                    ? deporteProp.GetString()
                                    : "";

                                eventos.Add(new
                                {
                                    IdEvento = idEvento,
                                    Nombre = nombre,
                                    Ciudad = ciudadResp,
                                    Asistentes = asistentes,
                                    Fecha = fecha,
                                    ValorEntrada = valorEntrada,
                                    TipoDeporte = tipoDeporteResp
                                });
                            }

                            // Mostrar en la tabla
                            dataGridView1.AutoGenerateColumns = false;
                            dataGridView1.DataSource = eventos;
                        }
                    }
                    else
                    {
                        string errorMsg = await response.Content.ReadAsStringAsync();
                        MessageBox.Show($"Código: {response.StatusCode}\nError: {errorMsg}");
                    }
                }
            }
    catch (Exception ex)
    {
                MessageBox.Show("Error al listar por parámetros: " + ex.Message);
            }

        }
    }
}
