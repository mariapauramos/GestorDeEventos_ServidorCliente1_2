using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
//Solo prueba de que este es el archivo final
namespace POCClienteEvento
{
    public partial class GUIPrincipal : Form
    {
        public GUIPrincipal()
        {
            InitializeComponent();
        }

        private void jMenuItemCrear_Click(object sender, EventArgs e)
        {
            GUICrearED gui = new GUICrearED();
            gui.Show();

        }

        private void jMenuItemSalir_Click(object sender, EventArgs e)
        {
            Application.Exit();

        }

        private void jMenuItemBuscar_Click(object sender, EventArgs e)
        {
            GUIBuscarED gui = new GUIBuscarED();
            gui.Show();
        }

        private void jMenuItemEliminar_Click(object sender, EventArgs e)
        {
            GUIEliminarED gui = new GUIEliminarED(); 
            gui.Show();
        }

        private void listarPorParametroToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GUIListarParametroED gui = new GUIListarParametroED();
            gui.Show();
        }

        private void jMenuItemListar_Click(object sender, EventArgs e)
        {
            GUIListarED gui = new GUIListarED();
            gui.Show();
        }

        private void jMenuItemActualizar_Click(object sender, EventArgs e)
        {
            GUIActualizarED gui = new GUIActualizarED();
            gui.Show();
        }

        private void jMenuItemAcerca_Click(object sender, EventArgs e)
        {
            GUIAcercaDe gui = new GUIAcercaDe();
            gui.Show();
        }
    }
}
