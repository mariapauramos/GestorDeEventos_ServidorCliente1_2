using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows.Forms;




namespace POCClienteEvento
{
    public partial class GUIListarED : Form
    {
        public GUIListarED()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

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
                    // Autenticación del servicio
                    var credentials = Convert.ToBase64String(System.Text.Encoding.ASCII.GetBytes("admin:admin"));
                    client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", credentials);

                    // URL del servidor
                    string url = "http://localhost:8091/eventos/ED";

                    // Petición GET al servidor
                    HttpResponseMessage response = await client.GetAsync(url);

                    if (response.IsSuccessStatusCode)
                    {
                        // Leer respuesta como string
                        var json = await response.Content.ReadAsStringAsync();

                        // Parsear con JsonDocument
                        using (JsonDocument doc = JsonDocument.Parse(json))
                        {
                            var eventos = new List<object>(); // lista genérica para cargar al DataGridView

                            foreach (var item in doc.RootElement.EnumerateArray())
                            {
                                // Aquí accedes a las propiedades del JSON
                                string idEvento = item.GetProperty("idEvento").GetString();
                                string nombre = item.GetProperty("nombre").GetString();
                                string ciudad = item.GetProperty("ciudad").GetString();
                                int asistentes = item.GetProperty("asistentes").GetInt32();
                                string fecha = item.GetProperty("fecha").GetString();
                                double valorEntrada = item.GetProperty("valorEntrada").GetDouble();

                                // Si existe tipoDeporte en el JSON
                                string tipoDeporte = item.TryGetProperty("tipoDeporte", out var deporteProp)
                                    ? deporteProp.GetString()
                                    : "";

                                // Crear objeto para mostrar en DataGridView
                                eventos.Add(new
                                {
                                    IdEvento = idEvento,
                                    Nombre = nombre,
                                    Ciudad = ciudad,
                                    Asistentes = asistentes,
                                    Fecha = fecha,
                                    ValorEntrada = valorEntrada,
                                    TipoDeporte = tipoDeporte
                                });
                            }

                            // Asignar la lista a la tabla
                            dataGridView1.AutoGenerateColumns = false  ;
                            dataGridView1.DataSource = eventos;


                        }
                    }
                    else
                    {
                        string errorMsg = await response.Content.ReadAsStringAsync();
                        MessageBox.Show($"Código: {response.StatusCode}\nError: {errorMsg}", "Error del servidor",
                            MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error al listar eventos: " + ex.Message);
            }

        }
    }
}
