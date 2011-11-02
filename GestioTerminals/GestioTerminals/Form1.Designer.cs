namespace GestioTerminals
{
    partial class Form1
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.btnEnvia = new System.Windows.Forms.Button();
            this.btnTerminal = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.listView1 = new System.Windows.Forms.ListView();
            this.gb = new System.Windows.Forms.GroupBox();
            this.rdSurtSessio = new System.Windows.Forms.RadioButton();
            this.rdReinicia = new System.Windows.Forms.RadioButton();
            this.rdApaga = new System.Windows.Forms.RadioButton();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.arxiuToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.buscaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.actualitzaScreenletToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.surtToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.accionsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.apagaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reiniciaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.surtSessioToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.enviaMissatgeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.updateUsersToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.gb.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(24, 55);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(463, 20);
            this.textBox1.TabIndex = 0;
            this.textBox1.Visible = false;
            // 
            // btnEnvia
            // 
            this.btnEnvia.Location = new System.Drawing.Point(512, 51);
            this.btnEnvia.Name = "btnEnvia";
            this.btnEnvia.Size = new System.Drawing.Size(75, 25);
            this.btnEnvia.TabIndex = 1;
            this.btnEnvia.Text = "Envia";
            this.btnEnvia.UseVisualStyleBackColor = true;
            this.btnEnvia.Visible = false;
            this.btnEnvia.Click += new System.EventHandler(this.btnEnvia_Click);
            // 
            // btnTerminal
            // 
            this.btnTerminal.Location = new System.Drawing.Point(593, 51);
            this.btnTerminal.Name = "btnTerminal";
            this.btnTerminal.Size = new System.Drawing.Size(75, 23);
            this.btnTerminal.TabIndex = 2;
            this.btnTerminal.Text = "Terminal";
            this.btnTerminal.UseVisualStyleBackColor = true;
            this.btnTerminal.Click += new System.EventHandler(this.btnTerminal_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(21, 39);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "label1";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 60000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "red");
            this.imageList1.Images.SetKeyName(1, "green");
            this.imageList1.Images.SetKeyName(2, "orange.png");
            // 
            // listView1
            // 
            this.listView1.Alignment = System.Windows.Forms.ListViewAlignment.SnapToGrid;
            this.listView1.AllowColumnReorder = true;
            this.listView1.AutoArrange = false;
            this.listView1.LabelWrap = false;
            this.listView1.LargeImageList = this.imageList1;
            this.listView1.Location = new System.Drawing.Point(24, 116);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(700, 360);
            this.listView1.TabIndex = 6;
            this.listView1.TileSize = new System.Drawing.Size(350, 350);
            this.listView1.UseCompatibleStateImageBehavior = false;
            // 
            // gb
            // 
            this.gb.Controls.Add(this.rdSurtSessio);
            this.gb.Controls.Add(this.rdReinicia);
            this.gb.Controls.Add(this.rdApaga);
            this.gb.Location = new System.Drawing.Point(435, 82);
            this.gb.Name = "gb";
            this.gb.Size = new System.Drawing.Size(288, 28);
            this.gb.TabIndex = 7;
            this.gb.TabStop = false;
            // 
            // rdSurtSessio
            // 
            this.rdSurtSessio.AutoSize = true;
            this.rdSurtSessio.Location = new System.Drawing.Point(170, 11);
            this.rdSurtSessio.Name = "rdSurtSessio";
            this.rdSurtSessio.Size = new System.Drawing.Size(75, 17);
            this.rdSurtSessio.TabIndex = 2;
            this.rdSurtSessio.TabStop = true;
            this.rdSurtSessio.Text = "SurtSessio";
            this.rdSurtSessio.UseVisualStyleBackColor = true;
            // 
            // rdReinicia
            // 
            this.rdReinicia.AutoSize = true;
            this.rdReinicia.Location = new System.Drawing.Point(37, 11);
            this.rdReinicia.Name = "rdReinicia";
            this.rdReinicia.Size = new System.Drawing.Size(63, 17);
            this.rdReinicia.TabIndex = 1;
            this.rdReinicia.TabStop = true;
            this.rdReinicia.Text = "Reinicia";
            this.rdReinicia.UseVisualStyleBackColor = true;
            // 
            // rdApaga
            // 
            this.rdApaga.AutoSize = true;
            this.rdApaga.Location = new System.Drawing.Point(106, 11);
            this.rdApaga.Name = "rdApaga";
            this.rdApaga.Size = new System.Drawing.Size(56, 17);
            this.rdApaga.TabIndex = 0;
            this.rdApaga.TabStop = true;
            this.rdApaga.Text = "Apaga";
            this.rdApaga.UseVisualStyleBackColor = true;
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.arxiuToolStripMenuItem,
            this.accionsToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(736, 24);
            this.menuStrip1.TabIndex = 8;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // arxiuToolStripMenuItem
            // 
            this.arxiuToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.buscaToolStripMenuItem,
            this.actualitzaScreenletToolStripMenuItem,
            this.surtToolStripMenuItem});
            this.arxiuToolStripMenuItem.Name = "arxiuToolStripMenuItem";
            this.arxiuToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.arxiuToolStripMenuItem.Text = "Arxiu";
            // 
            // buscaToolStripMenuItem
            // 
            this.buscaToolStripMenuItem.Name = "buscaToolStripMenuItem";
            this.buscaToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.buscaToolStripMenuItem.Text = "Busca";
            this.buscaToolStripMenuItem.Click += new System.EventHandler(this.buscaToolStripMenuItem_Click);
            // 
            // actualitzaScreenletToolStripMenuItem
            // 
            this.actualitzaScreenletToolStripMenuItem.Name = "actualitzaScreenletToolStripMenuItem";
            this.actualitzaScreenletToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.actualitzaScreenletToolStripMenuItem.Text = "Actualitza Screenlet";
            this.actualitzaScreenletToolStripMenuItem.Click += new System.EventHandler(this.actualitzaScreenletToolStripMenuItem_Click);
            // 
            // surtToolStripMenuItem
            // 
            this.surtToolStripMenuItem.Name = "surtToolStripMenuItem";
            this.surtToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.surtToolStripMenuItem.Text = "Surt";
            // 
            // accionsToolStripMenuItem
            // 
            this.accionsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.apagaToolStripMenuItem,
            this.reiniciaToolStripMenuItem,
            this.surtSessioToolStripMenuItem,
            this.enviaMissatgeToolStripMenuItem,
            this.updateUsersToolStripMenuItem});
            this.accionsToolStripMenuItem.Name = "accionsToolStripMenuItem";
            this.accionsToolStripMenuItem.Size = new System.Drawing.Size(55, 20);
            this.accionsToolStripMenuItem.Text = "Accions";
            // 
            // apagaToolStripMenuItem
            // 
            this.apagaToolStripMenuItem.Name = "apagaToolStripMenuItem";
            this.apagaToolStripMenuItem.Size = new System.Drawing.Size(156, 22);
            this.apagaToolStripMenuItem.Text = "Apaga";
            this.apagaToolStripMenuItem.Click += new System.EventHandler(this.apagaToolStripMenuItem_Click);
            // 
            // reiniciaToolStripMenuItem
            // 
            this.reiniciaToolStripMenuItem.Name = "reiniciaToolStripMenuItem";
            this.reiniciaToolStripMenuItem.Size = new System.Drawing.Size(156, 22);
            this.reiniciaToolStripMenuItem.Text = "Reinicia";
            this.reiniciaToolStripMenuItem.Click += new System.EventHandler(this.reiniciaToolStripMenuItem_Click);
            // 
            // surtSessioToolStripMenuItem
            // 
            this.surtSessioToolStripMenuItem.Name = "surtSessioToolStripMenuItem";
            this.surtSessioToolStripMenuItem.Size = new System.Drawing.Size(156, 22);
            this.surtSessioToolStripMenuItem.Text = "Surt Sessio";
            this.surtSessioToolStripMenuItem.Click += new System.EventHandler(this.surtSessioToolStripMenuItem_Click);
            // 
            // enviaMissatgeToolStripMenuItem
            // 
            this.enviaMissatgeToolStripMenuItem.Name = "enviaMissatgeToolStripMenuItem";
            this.enviaMissatgeToolStripMenuItem.Size = new System.Drawing.Size(156, 22);
            this.enviaMissatgeToolStripMenuItem.Text = "Envia Missatge";
            this.enviaMissatgeToolStripMenuItem.Click += new System.EventHandler(this.enviaMissatgeToolStripMenuItem_Click);
            // 
            // updateUsersToolStripMenuItem
            // 
            this.updateUsersToolStripMenuItem.Name = "updateUsersToolStripMenuItem";
            this.updateUsersToolStripMenuItem.Size = new System.Drawing.Size(156, 22);
            this.updateUsersToolStripMenuItem.Text = "Update Users";
            this.updateUsersToolStripMenuItem.Click += new System.EventHandler(this.updateUsersToolStripMenuItem_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(736, 549);
            this.Controls.Add(this.gb);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.btnTerminal);
            this.Controls.Add(this.btnEnvia);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.gb.ResumeLayout(false);
            this.gb.PerformLayout();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button btnEnvia;
        private System.Windows.Forms.Button btnTerminal;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.ImageList imageList1;
        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.GroupBox gb;
        private System.Windows.Forms.RadioButton rdReinicia;
        private System.Windows.Forms.RadioButton rdApaga;
        private System.Windows.Forms.RadioButton rdSurtSessio;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem arxiuToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem actualitzaScreenletToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem surtToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem buscaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem accionsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem apagaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reiniciaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem surtSessioToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem enviaMissatgeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem updateUsersToolStripMenuItem;
        
    }
}

