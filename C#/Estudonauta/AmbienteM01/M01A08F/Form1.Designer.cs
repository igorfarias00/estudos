namespace M01A08F
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btnOk = new Button();
            lblText = new Label();
            txtBox = new TextBox();
            lblMsg = new Label();
            SuspendLayout();
            // 
            // btnOk
            // 
            btnOk.Location = new Point(320, 174);
            btnOk.Name = "btnOk";
            btnOk.Size = new Size(156, 68);
            btnOk.TabIndex = 0;
            btnOk.Text = "Ok";
            btnOk.UseVisualStyleBackColor = true;
            btnOk.Click += btnOk_Click;
            // 
            // lblText
            // 
            lblText.AutoSize = true;
            lblText.Location = new Point(89, 83);
            lblText.Name = "lblText";
            lblText.Size = new Size(107, 15);
            lblText.TabIndex = 1;
            lblText.Text = "Digite um numero:";
            // 
            // txtBox
            // 
            txtBox.Location = new Point(205, 86);
            txtBox.Name = "txtBox";
            txtBox.Size = new Size(204, 23);
            txtBox.TabIndex = 2;
            // 
            // lblMsg
            // 
            lblMsg.AutoSize = true;
            lblMsg.Location = new Point(320, 324);
            lblMsg.Name = "lblMsg";
            lblMsg.Size = new Size(66, 15);
            lblMsg.TabIndex = 3;
            lblMsg.Text = "Mensagem";
            lblMsg.Visible = false;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(lblMsg);
            Controls.Add(txtBox);
            Controls.Add(lblText);
            Controls.Add(btnOk);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button btnOk;
        private Label lblText;
        private TextBox txtBox;
        private Label lblMsg;
    }
}