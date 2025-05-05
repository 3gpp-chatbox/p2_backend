-- Add resolution_reason column and update status enum
ALTER TABLE feedback 
ADD COLUMN resolution_reason TEXT,
ALTER COLUMN status TYPE VARCHAR(50) USING status::VARCHAR(50),
DROP CONSTRAINT IF EXISTS feedback_status_check,
ADD CONSTRAINT feedback_status_check CHECK (status IN ('pending', 'resolved')),
ADD COLUMN feedback_type VARCHAR(50) DEFAULT 'correction' CHECK (feedback_type IN ('correction', 'suggestion', 'question', 'clarification'));

-- Update existing records to use new status values
UPDATE feedback SET status = 'pending' WHERE status IN ('reviewed', 'addressed'); 