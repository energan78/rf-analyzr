import { useState } from 'react';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Container from '@mui/material/Container';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const SignalCapture = () => {
  const [frequency, setFrequency] = useState<number>(100);
  const [sampleRate, setSampleRate] = useState<number>(2);
  const [gain, setGain] = useState<number>(40);
  const [isCapturing, setIsCapturing] = useState(false);

  const chartData = {
    labels: Array.from({ length: 100 }, (_, i) => i.toString()),
    datasets: [
      {
        label: 'Signal Strength',
        data: Array.from({ length: 100 }, () => Math.random() * 100),
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }
    ]
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top' as const,
      },
      title: {
        display: true,
        text: 'Real-time Signal Visualization'
      }
    }
  };

  const handleStartCapture = () => setIsCapturing(true);
  const handleStopCapture = () => setIsCapturing(false);

  return (
    <Box sx={{ width: '100%' }}>
      <Card>
        <CardContent>
          <Typography variant="h5" gutterBottom>
            Signal Capture
          </Typography>
          <Container maxWidth="lg">
            <Stack spacing={2}>
              <Stack 
                direction={{ xs: 'column', md: 'row' }} 
                spacing={2} 
                sx={{ width: '100%' }}
              >
                <TextField
                  fullWidth
                  label="Frequency (MHz)"
                  type="number"
                  value={frequency}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => setFrequency(Number(e.target.value))}
                  disabled={isCapturing}
                />
                <TextField
                  fullWidth
                  label="Sample Rate (MHz)"
                  type="number"
                  value={sampleRate}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => setSampleRate(Number(e.target.value))}
                  disabled={isCapturing}
                />
                <TextField
                  fullWidth
                  label="Gain (dB)"
                  type="number"
                  value={gain}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => setGain(Number(e.target.value))}
                  disabled={isCapturing}
                />
              </Stack>
              
              <Box sx={{ mt: 3, mb: 3 }}>
                <Button
                  variant="contained"
                  color={isCapturing ? "error" : "primary"}
                  onClick={isCapturing ? handleStopCapture : handleStartCapture}
                  fullWidth
                >
                  {isCapturing ? "Stop Capture" : "Start Capture"}
                </Button>
              </Box>

              <Box sx={{ height: 400 }}>
                <Line options={chartOptions} data={chartData} />
              </Box>
            </Stack>
          </Container>
        </CardContent>
      </Card>
    </Box>
  );
};

export default SignalCapture;
