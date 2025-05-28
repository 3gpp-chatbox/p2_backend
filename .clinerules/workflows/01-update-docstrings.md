# Docstring Management Workflow

This workflow ensures documentation stays synchronized with code changes and maintains high quality standards across the project.

## File Analysis and Update Process

1. **Git Status Check:**

   - Identify modified Python files using `git status`
   - Focus on files with status M (modified), A (added), or ?? (untracked)

2. **Docstring Analysis:**

   - For each modified file:
     - Parse and analyze function/class/module docstrings
     - Compare docstrings with actual implementation
     - Check for:
       - Parameter changes
       - Return type changes
       - Function logic modifications
       - Missing docstrings

3. **Update Requirements:**

   - **Module Level:** Must include purpose, key components, and usage information
   - **Class Level:** Must document:
     - Class purpose
     - Attributes
     - Key methods
   - **Function Level:** Must maintain:
     - Clear description
     - Updated parameter list with types
     - Return value documentation
     - Raised exceptions
     - Usage examples for complex functions

4. **Format Standards:**

   - Follow Google-style docstring format
   - Include type hints in docstrings matching the code
   - Document exceptions with explanation
   - Keep docstrings concise but comprehensive

5. **Review Process:**

   - Present summary of proposed changes
   - Allow review before applying updates

6. **Quality Checks:**
   - Verify docstring completeness
   - Ensure parameter descriptions match implementation
   - Validate type hint consistency
   - Check for outdated examples or descriptions
