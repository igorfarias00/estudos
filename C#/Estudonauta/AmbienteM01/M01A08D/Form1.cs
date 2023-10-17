namespace M01A08D
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void btnOk_Click(object sender, EventArgs e)
        {
            int num = Convert.ToInt32(txtNum.Text);
            int dobro = num * 2;

            lblMsg.Text = "O dobro do numero é " + dobro;
            lblMsg.Visible = true;

        }
    }
}