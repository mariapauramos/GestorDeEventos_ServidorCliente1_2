namespace POCClienteEvento
{
    partial class GUIPrincipal
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(GUIPrincipal));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.jMenuArchivo = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuItemSalir = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuEvento = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuED = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuItemCrear = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuItemBuscar = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuItemListar = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuItemListarFiltro = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuItemActualizar = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuItemEliminar = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuAyuda = new System.Windows.Forms.ToolStripMenuItem();
            this.jMenuItemAcerca = new System.Windows.Forms.ToolStripMenuItem();
            this.pictureBox = new System.Windows.Forms.PictureBox();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.jMenuArchivo,
            this.jMenuEvento,
            this.jMenuAyuda});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(588, 26);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // jMenuArchivo
            // 
            this.jMenuArchivo.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.jMenuItemSalir});
            this.jMenuArchivo.Font = new System.Drawing.Font("Verdana", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.jMenuArchivo.Name = "jMenuArchivo";
            this.jMenuArchivo.Size = new System.Drawing.Size(80, 22);
            this.jMenuArchivo.Text = "Archivo";
            // 
            // jMenuItemSalir
            // 
            this.jMenuItemSalir.Name = "jMenuItemSalir";
            this.jMenuItemSalir.Size = new System.Drawing.Size(112, 22);
            this.jMenuItemSalir.Text = "Salir";
            this.jMenuItemSalir.Click += new System.EventHandler(this.jMenuItemSalir_Click);
            // 
            // jMenuEvento
            // 
            this.jMenuEvento.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.jMenuED});
            this.jMenuEvento.Font = new System.Drawing.Font("Verdana", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.jMenuEvento.Name = "jMenuEvento";
            this.jMenuEvento.Size = new System.Drawing.Size(76, 22);
            this.jMenuEvento.Text = "Evento";
            // 
            // jMenuED
            // 
            this.jMenuED.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.jMenuItemCrear,
            this.jMenuItemBuscar,
            this.jMenuItemListar,
            this.jMenuItemListarFiltro,
            this.jMenuItemActualizar,
            this.jMenuItemEliminar});
            this.jMenuED.Name = "jMenuED";
            this.jMenuED.Size = new System.Drawing.Size(217, 22);
            this.jMenuED.Text = "Evento Deportivo";
            // 
            // jMenuItemCrear
            // 
            this.jMenuItemCrear.Name = "jMenuItemCrear";
            this.jMenuItemCrear.Size = new System.Drawing.Size(199, 22);
            this.jMenuItemCrear.Text = "Crear";
            this.jMenuItemCrear.Click += new System.EventHandler(this.jMenuItemCrear_Click);
            // 
            // jMenuItemBuscar
            // 
            this.jMenuItemBuscar.Name = "jMenuItemBuscar";
            this.jMenuItemBuscar.Size = new System.Drawing.Size(199, 22);
            this.jMenuItemBuscar.Text = "Buscar";
            this.jMenuItemBuscar.Click += new System.EventHandler(this.jMenuItemBuscar_Click);
            // 
            // jMenuItemListar
            // 
            this.jMenuItemListar.Name = "jMenuItemListar";
            this.jMenuItemListar.Size = new System.Drawing.Size(199, 22);
            this.jMenuItemListar.Text = "Listar";
            this.jMenuItemListar.Click += new System.EventHandler(this.jMenuItemListar_Click);
            // 
            // jMenuItemListarFiltro
            // 
            this.jMenuItemListarFiltro.Name = "jMenuItemListarFiltro";
            this.jMenuItemListarFiltro.Size = new System.Drawing.Size(199, 22);
            this.jMenuItemListarFiltro.Text = "Listar por filtro";
            this.jMenuItemListarFiltro.Click += new System.EventHandler(this.listarPorParametroToolStripMenuItem_Click);
            // 
            // jMenuItemActualizar
            // 
            this.jMenuItemActualizar.Name = "jMenuItemActualizar";
            this.jMenuItemActualizar.Size = new System.Drawing.Size(199, 22);
            this.jMenuItemActualizar.Text = "Actualizar";
            this.jMenuItemActualizar.Click += new System.EventHandler(this.jMenuItemActualizar_Click);
            // 
            // jMenuItemEliminar
            // 
            this.jMenuItemEliminar.Name = "jMenuItemEliminar";
            this.jMenuItemEliminar.Size = new System.Drawing.Size(199, 22);
            this.jMenuItemEliminar.Text = "Eliminar";
            this.jMenuItemEliminar.Click += new System.EventHandler(this.jMenuItemEliminar_Click);
            // 
            // jMenuAyuda
            // 
            this.jMenuAyuda.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.jMenuItemAcerca});
            this.jMenuAyuda.Font = new System.Drawing.Font("Verdana", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.jMenuAyuda.Name = "jMenuAyuda";
            this.jMenuAyuda.Size = new System.Drawing.Size(70, 22);
            this.jMenuAyuda.Text = "Ayuda";
            // 
            // jMenuItemAcerca
            // 
            this.jMenuItemAcerca.Name = "jMenuItemAcerca";
            this.jMenuItemAcerca.Size = new System.Drawing.Size(180, 22);
            this.jMenuItemAcerca.Text = "Acerca de";
            this.jMenuItemAcerca.Click += new System.EventHandler(this.jMenuItemAcerca_Click);
            // 
            // pictureBox
            // 
            this.pictureBox.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox.Image")));
            this.pictureBox.Location = new System.Drawing.Point(103, 66);
            this.pictureBox.Name = "pictureBox";
            this.pictureBox.Size = new System.Drawing.Size(405, 231);
            this.pictureBox.TabIndex = 1;
            this.pictureBox.TabStop = false;
            // 
            // GUIPrincipal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(588, 381);
            this.Controls.Add(this.pictureBox);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "GUIPrincipal";
            this.Text = "Sistema Gestion de Eventos";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem jMenuArchivo;
        private System.Windows.Forms.ToolStripMenuItem jMenuItemSalir;
        private System.Windows.Forms.ToolStripMenuItem jMenuEvento;
        private System.Windows.Forms.ToolStripMenuItem jMenuED;
        private System.Windows.Forms.ToolStripMenuItem jMenuItemCrear;
        private System.Windows.Forms.ToolStripMenuItem jMenuItemBuscar;
        private System.Windows.Forms.ToolStripMenuItem jMenuItemListar;
        private System.Windows.Forms.ToolStripMenuItem jMenuItemActualizar;
        private System.Windows.Forms.ToolStripMenuItem jMenuItemEliminar;
        private System.Windows.Forms.ToolStripMenuItem jMenuAyuda;
        private System.Windows.Forms.ToolStripMenuItem jMenuItemAcerca;
        private System.Windows.Forms.PictureBox pictureBox;
        private System.Windows.Forms.ToolStripMenuItem jMenuItemListarFiltro;
    }
}

