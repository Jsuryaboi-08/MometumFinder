import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, ComposedChart, ReferenceDot } from 'recharts'
import api, { formatNumber, getSignalColor, getScoreColor } from '../services/api'

function StockDetail() {
    const { symbol } = useParams()
    const navigate = useNavigate()
    const [data, setData] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        fetchStockData()
    }, [symbol])

    const fetchStockData = async () => {
        try {
            setLoading(true)
            const result = await api.getStockDetail(symbol)
            setData(result)
            setError(null)
        } catch (err) {
            setError('Failed to load stock data. Please try again.')
            console.error(err)
        } finally {
            setLoading(false)
        }
    }

    if (loading) {
        return (
            <div className="flex justify-center items-center h-64 bg-gray-900">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-500"></div>
            </div>
        )
    }

    if (error || !data) {
        return (
            <div className="text-center py-12 bg-gray-900 min-h-screen">
                <h2 className="text-2xl font-bold text-gray-100 mb-4">Error Loading Data</h2>
                <p className="text-red-400 mb-6">{error || 'Stock not found'}</p>
                <button
                    onClick={() => navigate('/')}
                    className="bg-indigo-600 text-white px-6 py-2 rounded-lg hover:bg-indigo-700 transition"
                >
                    Go Back Home
                </button>
            </div>
        )
    }

    const { current, indicators, ratios } = data
    const signalColor = getSignalColor(current.signal)
    const scoreColor = getScoreColor(current.momentum_score)

    // Format history for chart - merging price and indicators
    const priceHistory = data.price_history ? [...data.price_history].reverse() : []
    const indicatorHistory = data.indicator_history ? [...data.indicator_history].reverse() : []

    // Create merged data for chart
    const chartData = priceHistory.map(price => {
        const ind = indicatorHistory.find(i => i.date === price.date)
        return {
            ...price,
            sma_20: ind?.sma_20,
            sma_50: ind?.sma_50,
            crossover: ind?.ma_crossovers?.find(c => c.date === price.date)
        }
    })

    // Prepare crossovers for easy plotting
    const crossovers = indicators?.ma_crossovers || []

    return (
        <div className="space-y-6 bg-gray-900 min-h-screen p-6">
            {/* Header Section */}
            <div className="bg-gray-800 rounded-xl shadow-lg p-6 border border-gray-700">
                <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                    <div>
                        <div className="flex items-center gap-3 mb-1">
                            <h1 className="text-3xl font-bold text-white">{data.symbol}</h1>
                            <span className="px-3 py-1 bg-gray-700 text-gray-300 text-sm font-medium rounded-full border border-gray-600">
                                {data.sector}
                            </span>
                        </div>
                        <p className="text-gray-400 text-lg">{data.name}</p>
                    </div>

                    <div className="flex items-center gap-6">
                        <div className="text-right">
                            <p className="text-sm text-gray-400 mb-1">Current Price</p>
                            <p className="text-3xl font-bold text-white">₹{formatNumber(current.price)}</p>
                            <p className="text-xs text-gray-500 mt-1">{new Date(current.date).toLocaleDateString()}</p>
                        </div>

                        <div className={`px-6 py-4 rounded-xl border ${signalColor.bg.replace('bg-', 'bg-opacity-20 bg-')} ${signalColor.border} backdrop-blur-sm`}>
                            <p className={`text-sm font-semibold mb-1 ${signalColor.text} uppercase tracking-wider`}>Signal</p>
                            <p className={`text-2xl font-bold ${signalColor.text}`}>{current.signal.replace('_', ' ')}</p>
                        </div>

                        <div className="px-6 py-4 rounded-xl border border-gray-700 bg-gray-800/50">
                            <p className="text-sm font-semibold text-gray-400 mb-1 uppercase tracking-wider">Momentum Score</p>
                            <p className={`text-3xl font-bold ${scoreColor.replace('text-', 'text-')}`}>{current.momentum_score}<span className="text-lg text-gray-600">/100</span></p>
                        </div>
                    </div>
                </div>
            </div>

            {/* Main Content Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

                {/* Left Column - Chart & Technicals */}
                <div className="lg:col-span-2 space-y-6">

                    {/* Price Chart */}
                    <div className="bg-gray-800 rounded-xl shadow-lg p-6 border border-gray-700">
                        <h2 className="text-xl font-bold text-white mb-4">Price Action & Moving Averages</h2>
                        <div className="h-80 w-full">
                            <ResponsiveContainer width="100%" height="100%">
                                <ComposedChart data={chartData}>
                                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#374151" />
                                    <XAxis
                                        dataKey="date"
                                        tickFormatter={(date) => new Date(date).toLocaleDateString(undefined, { month: 'short', day: 'numeric' })}
                                        axisLine={false}
                                        tickLine={false}
                                        tick={{ fontSize: 12, fill: '#9ca3af' }}
                                        minTickGap={30}
                                    />
                                    <YAxis
                                        domain={['auto', 'auto']}
                                        axisLine={false}
                                        tickLine={false}
                                        tick={{ fontSize: 12, fill: '#9ca3af' }}
                                        tickFormatter={(val) => `₹${val}`}
                                    />
                                    <Tooltip
                                        contentStyle={{ backgroundColor: '#1f2937', borderRadius: '8px', border: '1px solid #374151', color: '#f3f4f6' }}
                                        itemStyle={{ color: '#e5e7eb' }}
                                        labelFormatter={(label) => new Date(label).toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
                                        formatter={(value, name) => [
                                            `₹${formatNumber(value)}`,
                                            name === 'close' ? 'Price' : name === 'sma_20' ? 'SMA 20' : name === 'sma_50' ? 'SMA 50' : name
                                        ]}
                                    />
                                    <Area
                                        type="monotone"
                                        dataKey="close"
                                        stroke="#818cf8"
                                        fill="#312e81"
                                        fillOpacity={0.3}
                                        strokeWidth={2}
                                        name="Price"
                                    />
                                    <Line
                                        type="monotone"
                                        dataKey="sma_20"
                                        stroke="#fbbf24"
                                        strokeWidth={2}
                                        dot={false}
                                        strokeDasharray="5 5"
                                        name="SMA 20"
                                        connectNulls
                                    />
                                    <Line
                                        type="monotone"
                                        dataKey="sma_50"
                                        stroke="#f87171"
                                        strokeWidth={2}
                                        dot={false}
                                        name="SMA 50"
                                        connectNulls
                                    />
                                    {/* Render Crossover Points */}
                                    {crossovers.map((cross, idx) => (
                                        <ReferenceDot
                                            key={idx}
                                            x={cross.date}
                                            y={cross.sma_20}
                                            r={5}
                                            fill={cross.type === 'golden_cross' ? '#22c55e' : '#ef4444'}
                                            stroke="#fff"
                                            strokeWidth={2}
                                            label={cross.type === 'golden_cross' ? 'Golden' : 'Death'}
                                        />
                                    ))}
                                </ComposedChart>
                            </ResponsiveContainer>
                        </div>

                        <div className="mt-4 flex flex-wrap gap-4 text-sm text-gray-400">
                            <div className="flex items-center gap-2">
                                <span className="w-3 h-3 rounded-full bg-indigo-400"></span> Price
                            </div>
                            <div className="flex items-center gap-2">
                                <span className="w-3 h-3 rounded-full bg-yellow-400"></span> SMA 20
                            </div>
                            <div className="flex items-center gap-2">
                                <span className="w-3 h-3 rounded-full bg-red-400"></span> SMA 50
                            </div>
                            {crossovers.length > 0 && (
                                <div className="flex items-center gap-2 ml-auto">
                                    <span className="w-2 h-2 rounded-full bg-green-500"></span> Golden Cross
                                    <span className="w-2 h-2 rounded-full bg-red-500 ml-2"></span> Death Cross
                                </div>
                            )}
                        </div>
                    </div>

                    {/* Ratios Grid */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {/* Fundamental Ratios */}
                        <div className="bg-gray-800 rounded-xl shadow-lg p-6 border border-gray-700">
                            <h3 className="text-lg font-bold text-gray-100 mb-4 flex items-center gap-2">
                                <span className="text-indigo-400">📊</span> Fundamental Ratios
                            </h3>
                            <div className="space-y-4">
                                <RatioItem
                                    label="P/E Ratio"
                                    value={ratios?.pe_ratio}
                                    ideal="8-20"
                                    tooltip="Price to Earnings. 8-20 is typically considered fair value."
                                />
                                <RatioItem
                                    label="P/B Ratio"
                                    value={ratios?.pb_ratio}
                                    ideal="0.5-3.0"
                                    tooltip="Price to Book. Lower is better value."
                                />
                                <RatioItem
                                    label="ROE"
                                    value={ratios?.roe}
                                    suffix="%"
                                    ideal=">15%"
                                    tooltip="Return on Equity. Higher is better."
                                />
                                <RatioItem
                                    label="Debt/Equity"
                                    value={ratios?.debt_to_equity}
                                    ideal="<1.0"
                                    tooltip="Debt to Equity ratio. Lower means less leverage."
                                />
                                <RatioItem
                                    label="Current Ratio"
                                    value={ratios?.current_ratio}
                                    ideal="1.5-2.5"
                                    tooltip="Measures liquidity. Higher is safer."
                                />
                            </div>
                        </div>

                        {/* Trading Ratios */}
                        <div className="bg-gray-800 rounded-xl shadow-lg p-6 border border-gray-700">
                            <h3 className="text-lg font-bold text-gray-100 mb-4 flex items-center gap-2">
                                <span className="text-orange-400">📈</span> Trading Ratios
                            </h3>
                            <div className="space-y-4">
                                <RatioItem
                                    label="EPS (TTM)"
                                    value={ratios?.eps}
                                    tooltip="Earnings Per Share (Trailing Twelve Months)"
                                />
                                <RatioItem
                                    label="Beta"
                                    value={ratios?.beta}
                                    ideal="0.8-1.2"
                                    tooltip="Volatility relative to market. 1.0 is market average."
                                />
                                <RatioItem
                                    label="52W Position"
                                    value={ratios?.week_52_position}
                                    suffix="%"
                                    ideal=">60%"
                                    tooltip="Position within 52-week range (0% = Low, 100% = High)"
                                />
                                <RatioItem
                                    label="Avg Volume"
                                    value={ratios?.avg_volume ? formatNumber(ratios.avg_volume) : 'N/A'}
                                    tooltip="Average daily trading volume"
                                />
                                <RatioItem
                                    label="Market Cap"
                                    value={ratios?.market_cap_category}
                                    tooltip="Size category (Large, Mid, Small Cap)"
                                />
                            </div>
                        </div>
                    </div>

                    {/* Signal Rationale */}
                    <div className="bg-gray-800 rounded-xl shadow-lg p-6 border border-gray-700">
                        <h3 className="text-lg font-bold text-gray-100 mb-3">Signal Rationale</h3>
                        <p className="text-gray-300 leading-relaxed">{current.signal_rationale}</p>
                    </div>

                </div>

                {/* Right Column - Score Breakdown */}
                <div className="space-y-6">
                    <div className="bg-gray-800 rounded-xl shadow-lg p-6 border border-gray-700">
                        <h2 className="text-xl font-bold text-white mb-4">Score Breakdown</h2>
                        <div className="space-y-0 divide-y divide-gray-700">
                            {Object.entries(data.score_breakdown)
                                .filter(([key]) => key !== 'total_score')
                                .map(([key, item]) => (
                                    <ScoreBreakdownItem key={key} name={key} data={item} />
                                ))}
                        </div>
                    </div>

                    <div className="bg-gray-800 rounded-xl shadow-lg p-6 border border-gray-700">
                        <h2 className="text-xl font-bold text-white mb-4">Key Levels</h2>
                        <div className="space-y-4">
                            <PriceLevel label="Current" price={current.price} isCurrent />
                            <PriceLevel label="52W High" price={ratios?.week_52_high} />
                            <PriceLevel label="52W Low" price={ratios?.week_52_low} />
                            <div className="pt-4 border-t border-gray-700">
                                <h4 className="text-sm font-semibold text-gray-500 mb-3">Technical Levels</h4>
                                <PriceLevel label="SMA 20" price={indicators.sma_20} />
                                <PriceLevel label="SMA 50" price={indicators.sma_50} />
                                <PriceLevel label="Upper BB" price={indicators.bb_upper} />
                                <PriceLevel label="Lower BB" price={indicators.bb_lower} />
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    )
}

function RatioItem({ label, value, suffix = '', ideal, tooltip }) {
    if (value === undefined || value === null) return null

    return (
        <div className="flex justify-between items-center group relative cursor-help py-1">
            <div className="text-gray-400 font-medium border-b border-dashed border-gray-600 hover:border-gray-400 transition-colors">
                {label}
                {tooltip && (
                    <div className="absolute left-0 bottom-full mb-2 hidden group-hover:block w-48 p-2 bg-gray-900 border border-gray-700 text-gray-200 text-xs rounded z-10 shadow-xl">
                        {tooltip}
                    </div>
                )}
            </div>
            <div className="text-right">
                <div className="font-bold text-gray-200">
                    {typeof value === 'number' ? formatNumber(value) : value}{suffix}
                </div>
                {ideal && <div className="text-xs text-indigo-400">Target: {ideal}</div>}
            </div>
        </div>
    )
}

function ScoreBreakdownItem({ name, data }) {
    const displayName = {
        'roc_5': 'ROC (5d)',
        'roc_10': 'ROC (10d)',
        'roc_20': 'ROC (20d)',
        'relative_strength': 'Rel Strength',
        'volume': 'Volume',
        'rsi': 'RSI',
        'ma': 'Mov Avg',
        'fundamental': 'Fundamentals',
        'trading': 'Trading Ratios'
    }[name] || name

    const scoreColor = data.score >= 70 ? 'text-green-400' :
        data.score >= 50 ? 'text-yellow-400' : 'text-red-400'

    const barColor = data.score >= 70 ? 'bg-green-500' :
        data.score >= 50 ? 'bg-yellow-500' : 'bg-red-500'

    return (
        <div className="py-3 first:pt-0 last:pb-0">
            <div className="flex justify-between items-center mb-1">
                <span className="text-sm font-medium text-gray-300">{displayName}</span>
                <span className={`text-sm font-bold ${scoreColor}`}>{data.score}</span>
            </div>
            <div className="w-full bg-gray-700 rounded-full h-2 overflow-hidden">
                <div
                    className={`h-full rounded-full ${barColor}`}
                    style={{ width: `${data.score}%` }}
                ></div>
            </div>
            <div className="flex justify-between text-xs text-gray-500 mt-1">
                <span>Weight: {Math.round(data.weight * 100)}%</span>
                <span>Contrib: {data.contribution}</span>
            </div>
        </div>
    )
}

function PriceLevel({ label, price, isCurrent = false }) {
    if (!price) return null
    return (
        <div className={`flex justify-between items-center ${isCurrent ? 'bg-indigo-900/30 p-2 rounded-lg -mx-2' : ''}`}>
            <span className={`text-sm ${isCurrent ? 'font-bold text-indigo-300' : 'text-gray-400'}`}>{label}</span>
            <span className={`font-mono ${isCurrent ? 'font-bold text-indigo-300' : 'text-gray-200'}`}>
                ₹{formatNumber(price)}
            </span>
        </div>
    )
}

export default StockDetail
