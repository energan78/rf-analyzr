import { useState, useCallback } from 'react';
import { SignalInfo, SignalsResponse, SignalsByFrequencyResponse } from '../types/signals';

const API_BASE = 'http://localhost:5000';

export function useSignals() {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [signals, setSignals] = useState<SignalInfo[]>([]);
    
    const getAllSignals = useCallback(async () => {
        try {
            setLoading(true);
            setError(null);
            const response = await fetch(`${API_BASE}/api/signals`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data: SignalsResponse = await response.json();
            setSignals(data.signals);
        } catch (e) {
            setError(e instanceof Error ? e.message : 'Неизвестная ошибка');
        } finally {
            setLoading(false);
        }
    }, []);

    const findSignalsByFrequency = useCallback(async (frequency: number) => {
        try {
            setLoading(true);
            setError(null);
            const response = await fetch(`${API_BASE}/api/signals?freq=${frequency}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data: SignalsByFrequencyResponse = await response.json();
            setSignals(data.signals);
            return data.signals;
        } catch (e) {
            setError(e instanceof Error ? e.message : 'Неизвестная ошибка');
            return [];
        } finally {
            setLoading(false);
        }
    }, []);

    return {
        signals,
        loading,
        error,
        getAllSignals,
        findSignalsByFrequency,
    };
}
