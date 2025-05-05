CREATE TABLE IF NOT EXISTS feedback (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    graph_id UUID NOT NULL REFERENCES graph(id) ON DELETE CASCADE,
    comment TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    user_email VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending' CHECK (status IN ('pending', 'reviewed', 'addressed'))
);

-- Create index for faster queries
CREATE INDEX IF NOT EXISTS idx_feedback_graph_id ON feedback(graph_id);
CREATE INDEX IF NOT EXISTS idx_feedback_status ON feedback(status); 