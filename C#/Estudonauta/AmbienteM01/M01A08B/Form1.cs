namespace M01A08B
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string nome = txtNome.Text;
            lblMsg.Text = "Muito Prazer em te conhecer, " + nome + "!";
            lblMsg.Visible = true;
        }
    }
}